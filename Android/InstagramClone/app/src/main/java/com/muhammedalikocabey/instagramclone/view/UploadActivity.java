package com.muhammedalikocabey.instagramclone.view;


import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Toast;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.material.snackbar.BaseTransientBottomBar;
import com.google.android.material.snackbar.Snackbar;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.FieldValue;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.UploadTask;
import com.muhammedalikocabey.instagramclone.databinding.ActivityUploadBinding;

import java.util.HashMap;
import java.util.UUID;


public class UploadActivity extends AppCompatActivity {

    private ActivityUploadBinding binding;

    private ActivityResultLauncher<Intent> activityResultLauncher;
    private ActivityResultLauncher<String> permissionLauncher;

    private Uri imageData;

    private Bitmap selectedBitmap;


    private FirebaseStorage firebaseStorage;
    private FirebaseAuth firebaseAuth;
    private FirebaseFirestore firebaseFirestore;
    private StorageReference storageReference;
    private FirebaseUser firebaseUser;
    private String firebaseUserID;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityUploadBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        registerLauncher();


        firebaseStorage = FirebaseStorage.getInstance();
        firebaseAuth = FirebaseAuth.getInstance();
        firebaseFirestore = FirebaseFirestore.getInstance();
        storageReference = firebaseStorage.getReference();
        firebaseUser = firebaseAuth.getCurrentUser();

        if(firebaseUser != null) {
            firebaseUserID = firebaseUser.getUid();
        } else {
            firebaseUserID = "default";
        }

        binding.uploadButton.setEnabled(false);
    }



    public void uploadButtonClicked(View view)  {

        if(imageData != null) {

            UUID imageUUID = UUID.randomUUID();
            String imageDataName = "images/" + firebaseUserID + "/" + imageUUID + ".jpg";

            storageReference.child(imageDataName).putFile(imageData).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
                @Override
                public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
                    StorageReference newReference = firebaseStorage.getReference(imageDataName);

                    newReference.getDownloadUrl().addOnSuccessListener(new OnSuccessListener<Uri>() {
                        @Override
                        public void onSuccess(Uri uri) {
                            String downloadUrl = uri.toString();

                            String comment = binding.commentText.getText().toString();

                            String email = firebaseUser.getEmail();

                            HashMap<String, Object> postData = new HashMap<>();
                            postData.put("user_email", email);
                            postData.put("download_url", downloadUrl);
                            postData.put("comment", comment);
                            postData.put("date", FieldValue.serverTimestamp());

                            firebaseFirestore.collection("Posts").add(postData).addOnSuccessListener(new OnSuccessListener<DocumentReference>() {
                                @Override
                                public void onSuccess(DocumentReference documentReference) {
                                    Intent intent = new Intent(UploadActivity.this, FeedActivity.class);
                                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                                    startActivity(intent);
                                }
                            }).addOnFailureListener(new OnFailureListener() {
                                @Override
                                public void onFailure(@NonNull Exception e) {
                                    Toast.makeText(UploadActivity.this, e.getLocalizedMessage(), Toast.LENGTH_LONG).show();
                                }
                            });

                        }
                    }).addOnFailureListener(new OnFailureListener() {
                        @Override
                        public void onFailure(@NonNull Exception e) {
                            Toast.makeText(UploadActivity.this, e.getLocalizedMessage(), Toast.LENGTH_LONG).show();
                        }
                    });
                }
            }).addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    Toast.makeText(UploadActivity.this, e.getLocalizedMessage(), Toast.LENGTH_LONG).show();
                }
            });

        }


    }


    public void selectImage(View view) {

        if(ContextCompat.checkSelfPermission(UploadActivity.this, Manifest.permission.READ_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {

            if(ActivityCompat.shouldShowRequestPermissionRationale(UploadActivity.this, Manifest.permission.READ_EXTERNAL_STORAGE)) {
                Snackbar.make(view, "Permission Needed for Gallery", BaseTransientBottomBar.LENGTH_INDEFINITE).setAction("Give Permission", new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        // ask permission
                        permissionLauncher.launch(Manifest.permission.READ_EXTERNAL_STORAGE);
                    }
                }).show();
            }

            else {
                // ask permission
                permissionLauncher.launch(Manifest.permission.READ_EXTERNAL_STORAGE);
            }
        }
        else {
            // Permission Granted
            Intent intentToGallery = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
            activityResultLauncher.launch(intentToGallery);
        }




    }



    private void registerLauncher() {

        activityResultLauncher = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(), new ActivityResultCallback<ActivityResult>() {
            @Override
            public void onActivityResult(ActivityResult result) {
                if(result.getResultCode() == RESULT_OK) {
                    Intent intentFromResult = result.getData();

                    if(intentFromResult != null) {
                        imageData = intentFromResult.getData();


                        binding.imageView.setImageURI(imageData);
                        binding.uploadButton.setEnabled(true);

                        /*
                        try {

                            if(Build.VERSION.SDK_INT >= 28) {
                                ImageDecoder.Source source = ImageDecoder.createSource(UploadActivity.this.getContentResolver(), imageData);
                                selectedBitmap = ImageDecoder.decodeBitmap(source);
                                binding.imageView.setImageBitmap(selectedBitmap);
                            } else {
                                selectedBitmap = MediaStore.Images.Media.getBitmap(UploadActivity.this.getContentResolver(), imageData);
                                binding.imageView.setImageBitmap(selectedBitmap);
                            }

                        } catch (Exception e) {
                            e.printStackTrace();
                        }

                         */
                    }
                }
            }
        });



        permissionLauncher = registerForActivityResult(new ActivityResultContracts.RequestPermission(), new ActivityResultCallback<Boolean>() {
            @Override
            public void onActivityResult(Boolean result) {
                if(result) {
                    Intent intentToGallery = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
                    activityResultLauncher.launch(intentToGallery);

                } else {
                    Toast.makeText(UploadActivity.this, "Permission Denied, We Need Permission", Toast.LENGTH_LONG).show();
                }
            }
        });

    }


}