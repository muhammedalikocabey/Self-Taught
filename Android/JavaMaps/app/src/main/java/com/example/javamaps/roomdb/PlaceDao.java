package com.example.javamaps.roomdb;


import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.Query;

import com.example.javamaps.model.Place;

import java.util.List;

import io.reactivex.rxjava3.core.Completable;
import io.reactivex.rxjava3.core.Flowable;


@Dao
public interface PlaceDao {

    @Insert
    Completable insert(Place place);

    @Delete
    Completable delete(Place place);

    @Query("SELECT * FROM place")
    Flowable<List<Place>> getAll();
}
