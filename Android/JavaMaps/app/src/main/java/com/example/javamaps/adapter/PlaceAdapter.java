package com.example.javamaps.adapter;

import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.javamaps.databinding.ReyclerRowBinding;
import com.example.javamaps.model.Place;
import com.example.javamaps.view.MapsActivity;

import java.util.List;

public class PlaceAdapter extends RecyclerView.Adapter<PlaceAdapter.PlaceHolder> {

    List<Place> placeList;

    public PlaceAdapter(List<Place> placeList) {
        this.placeList = placeList;
    }

    @NonNull
    @Override
    public PlaceHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        ReyclerRowBinding reyclerRowBinding = ReyclerRowBinding.inflate(LayoutInflater.from(parent.getContext()), parent, false);
        return new PlaceHolder(reyclerRowBinding);
    }

    @Override
    public void onBindViewHolder(@NonNull PlaceHolder holder, int position) {
        holder.reyclerRowBinding.recyclerViewTextView.setText(placeList.get(position).name);

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(holder.itemView.getContext(), MapsActivity.class);
                intent.putExtra("info", "old");
                intent.putExtra("place", placeList.get(position));
                holder.itemView.getContext().startActivity(intent);
            }
        });
    }

    @Override
    public int getItemCount() {
        return placeList.size();
    }


    public class PlaceHolder extends RecyclerView.ViewHolder {
        ReyclerRowBinding reyclerRowBinding;

        public PlaceHolder(ReyclerRowBinding reyclerRowBinding) {
            super(reyclerRowBinding.getRoot());
            this.reyclerRowBinding = reyclerRowBinding;
        }
    }
}
