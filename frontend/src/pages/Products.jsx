import { useState } from "react";
import Grid from "@mui/material/Grid";
import DataTable from "../components/DataTable";

export default function Products() {
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [selectedFeature, setSelectedFeature] = useState(null);
  const [selectedProduct, setSelectedProduct] = useState(null);

  return (
    <Grid container spacing={2} mt={0} ml={-5}>
      {/* Category */}
      <Grid item xs={4}>
        <DataTable
          modelName="category"
          onRowSelected={(selectedCategory) => {
            console.log("Selected category:", selectedCategory);
            setSelectedCategory(selectedCategory);
          }}
          baseModel={{ name: "new category" }}
        />
      </Grid>
      {/* Feature */}
      {selectedCategory && (
        <Grid item xs={4}>
          <DataTable
            modelName="feature"
            queryParams={{ category: selectedCategory.id }}
            onRowSelected={(selectedFeature) => {
              console.log("Selected Feature:", selectedFeature);
              setSelectedFeature(selectedFeature);
            }}
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
            onRowSelected={(selectedProduct) => {
              console.log("Selected Product:", selectedProduct);
              setSelectedProduct(selectedProduct);
            }}
            queryParams={
              selectedCategory ? { category: selectedCategory.id } : {}
            }
          />
        </Grid>
      )}
      {selectedCategory && selectedProduct && selectedFeature && (
        <Grid item xs={6}>
          <DataTable
            modelName="productfeature"
            queryParams={{
              product: selectedProduct.id,
              category: selectedCategory.id,
            }}
            baseModel={{
              product: selectedProduct.id,
              feature: selectedFeature.id,
              value: "new value",
            }}
          />
        </Grid>
      )}
    </Grid>
  );
}
