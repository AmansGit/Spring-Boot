package com.database.bootjpa.dao;

import com.database.bootjpa.model.AmanBrand;
import org.springframework.data.repository.CrudRepository;

public interface AmanRepo extends CrudRepository<AmanBrand, Integer> {
}
