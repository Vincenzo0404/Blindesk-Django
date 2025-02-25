import { useState, useEffect } from "react";
import Grid from "@mui/material/Grid";
import api from "../api";
import DataTable from "../components/DataTable";

export default function Products() {
  const [suppliers, setSuppliers] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);

  useEffect(() => {
    const fetchSuppliers = async () => {
      try {
        const response = await api.get("/api/supplier/list/");
        setSuppliers(response.data);
      } catch (error) {
        console.error("Error fetching suppliers:", error);
      }
    };
    fetchSuppliers();
  }, []);

  return (
    <Grid container spacing={3} mt={2}>
      {/* Category */}
      <Grid item xs={4}>
        <DataTable
          modelName="category"
          onRowSelected={(selectedCategory) => {
            setSelectedCategory(selectedCategory);
          }}
        />
      </Grid>
      {/* Feature */}
      {selectedCategory && (
        <Grid item xs={4}>
          <DataTable
            modelName="feature"
            queryParams={{ category: selectedCategory.id }}
            baseModel={{ category: selectedCategory.id, name: "new feature" }}
          />
        </Grid>
      )}

      {/* Product */}

      {selectedCategory && (
        <Grid item xs={4}>
          <DataTable
            modelName="product"
            baseModel={{
              name: "new product",
              category: selectedCategory.id,
              supplier: 1,
            }}
            queryParams={
              selectedCategory ? { category: selectedCategory.id } : {}
            }
          />
        </Grid>
      )}
    </Grid>
  );
}
