import { useState, useEffect } from "react";
import { TextField, Button, FormControl, Autocomplete } from "@mui/material";
import api from "../api";

const JobForm = (onClose) => {
  const [customers, setCustomers] = useState([]);
  const [formData, setFormData] = useState({
    customer: "",
    stage: "",
    created_at: "",
  });

  useEffect(() => {
    api
      .get("/api/customer/list/")
      .then((response) => setCustomers(response.data))
      .catch((error) => console.error("Error fetching customers:", error));
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleCustomerChange = (event, value) => {
    setFormData({
      ...formData,
      customer: value ? value.id : "",
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    api
      .post("/api/job/create/", formData)
      .then((response) => {
        if (response.data.success) {
          onClose();
        } else {
          console.error("Error creating job:", response.data.errors);
        }
      })
      .catch((error) => console.error("Error creating job:", error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <FormControl fullWidth margin="normal">
        <Autocomplete
          options={customers}
          getOptionLabel={(option) => `${option.name} ${option.surname}`}
          onChange={handleCustomerChange}
          renderInput={(params) => <TextField {...params} label="Customer" />}
        />
      </FormControl>
      <Button type="submit" variant="contained" color="primary">
        Submit
      </Button>
      <Button onClick={onClose} variant="outlined" color="secondary">
        Cancel
      </Button>
    </form>
  );
};

export default JobForm;
