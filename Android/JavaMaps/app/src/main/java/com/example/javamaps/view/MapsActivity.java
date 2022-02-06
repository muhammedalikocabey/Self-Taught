package com.example.javamaps.view;

import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.FragmentActivity;
import androidx.room.Room;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import com.example.javamaps.R;
import com.example.javamaps.databinding.ActivityMapsBinding;
import com.example.javamaps.model.Place;
import com.example.javamaps.roomdb.PlaceDao;
import com.example.javamaps.roomdb.PlaceDatabase;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.material.snackbar.Snackbar;

import io.reactivex.rxjava3.android.schedulers.AndroidSchedulers;
import io.reactivex.rxjava3.disposables.CompositeDisposable;
import io.reactivex.rxjava3.disposables.Disposable;
import io.reactivex.rxjava3.schedulers.Schedulers;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback, GoogleMap.OnMapLongClickListener {

    private GoogleMap mMap;
    private ActivityMapsBinding binding;
    private ActivityResultLauncher<String> permissionLauncher;

    private LocationManager locationManager;
    private LocationListener locationListener;

    private SharedPreferences sharedPreferences;
    boolean info;

    private PlaceDatabase placeDatabase;
    private PlaceDao placeDao;

    private Double selectedLatitude;
    private Double selectedLongitude;

    private CompositeDisposable compositeDisposable = new CompositeDisposable();

    Place selectedPlace;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMapsBinding.inflate(getLayoutInflater());
        View view = binding.getRoot();
        setContentView(view);

        // setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        registerLauncher();

        sharedPreferences = MapsActivity.this.getSharedPreferences("com.example.javamaps", MODE_PRIVATE);
        info = false;

        placeDatabase = Room.databaseBuilder(getApplicationContext(), PlaceDatabase.class, "place")
                .allowMainThreadQueries()
                .build();
        placeDao = placeDatabase.placeDao();

        selectedLatitude = 0.0;
        selectedLongitude = 0.0;

        binding.saveButton.setEnabled(false);

    }


    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        mMap.setOnMapLongClickListener(MapsActivity.this);


        Intent intent = getIntent();
        String intentInfo = intent.getStringExtra("info");

        if(intentInfo.equals("new")) {

            binding.saveButton.setVisibility(View.VISIBLE);
            binding.deleteButton.setVisibility(View.GONE);


            locationManager = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);
            locationListener = new LocationListener() {
                @Override
                public void onLocationChanged(@NonNull Location location) {


                    info = sharedPreferences.getBoolean("info", false);



                    if(!info) {
                        LatLng userLocation = new LatLng(location.getLatitude(), location.getLongitude());
                        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(userLocation, 15f));
                        sharedPreferences.edit().putBoolean("info", true).apply();
                    }
                }

            };


            // locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, locationListener);

            if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {

                if (ActivityCompat.shouldShowRequestPermissionRationale(this, Manifest.permission.ACCESS_FINE_LOCATION)) {
                    Snackbar.make(binding.getRoot(), "Permission needed for maps", Snackbar.LENGTH_INDEFINITE).setAction("Give Permission", new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            permissionLauncher.launch(Manifest.permission.ACCESS_FINE_LOCATION);
                        }
                    });
                } else {
                    permissionLauncher.launch(Manifest.permission.ACCESS_FINE_LOCATION);
                }
            } else {
                locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, locationListener);

                Location lastLocation = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
                if(lastLocation != null) {
                    LatLng lastUserLocation = new LatLng(lastLocation.getLatitude(), lastLocation.getLongitude());
                    mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(lastUserLocation, 15f));
                }

                mMap.setMyLocationEnabled(true);

            }

        } else {

            mMap.clear();

            selectedPlace = (Place) intent.getSerializableExtra("place");

            LatLng latLng = new LatLng(selectedPlace.latitude, selectedPlace.longitude);

            mMap.addMarker(new MarkerOptions().position(latLng).title(selectedPlace.name));
            mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(latLng, 16f));

            binding.placeNameText.setText(selectedPlace.name);
            binding.saveButton.setVisibility(View.GONE);
            binding.deleteButton.setVisibility(View.VISIBLE);
        }

    }



    private void registerLauncher() {
        permissionLauncher = registerForActivityResult(new ActivityResultContracts.RequestPermission(), new ActivityResultCallback<Boolean>() {
            @Override
            public void onActivityResult(Boolean result) {
                if (result) {
                    if (ActivityCompat.checkSelfPermission(MapsActivity.this, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED &&
                            ActivityCompat.checkSelfPermission(MapsActivity.this, Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED) {

                        // permission granted
                        locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, locationListener);

                        Location lastLocation = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
                        if(lastLocation != null) {
                            LatLng lastUserLocation = new LatLng(lastLocation.getLatitude(), lastLocation.getLongitude());
                            mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(lastUserLocation, 15f));
                        }
                    }

                } else {
                    Toast.makeText(MapsActivity.this, "Permission Denied. Permission Needed!", Toast.LENGTH_LONG).show();
                }
            }
        });
    }



    @Override
    public void onMapLongClick(LatLng latLng) {
        mMap.clear();
        mMap.addMarker(new MarkerOptions().position(latLng));

        selectedLatitude = latLng.latitude;
        selectedLongitude = latLng.longitude;

        binding.saveButton.setEnabled(true);
    }



    public void save(View view) {
        Place newPlace = new Place(binding.placeNameText.getText().toString(), selectedLatitude, selectedLongitude);

        /*
        Threading ->
            Main    (UI)                    Thread,
            Default (CPU Intensive)         Thread
            IO      (Network, Database)     Thread

         */

        //placeDao.insert(newPlace).subscribeOn(Schedulers.io()).subscribe();

        compositeDisposable.add(placeDao.insert(newPlace)
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(MapsActivity.this::handleResponse)
        );

    }



    private void handleResponse() {
        Intent intent = new Intent(MapsActivity.this, MainActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
        startActivity(intent);
    }



    public void delete(View view) {

        if(selectedPlace != null) {
            compositeDisposable.add(placeDao.delete(selectedPlace)
                    .subscribeOn(Schedulers.io())
                    .observeOn(AndroidSchedulers.mainThread())
                    .subscribe(MapsActivity.this::handleResponse)
            );
        }

    }



    @Override
    protected void onDestroy() {
        super.onDestroy();

        compositeDisposable.clear();
    }
}