import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import {
  TextField,
  FormControl,
  Autocomplete,
  MenuItem,
  Select,
  InputLabel,
} from "@mui/material";
import api from "../api";
import Form from "./Form";

const cities = ["Roma", "Aquila"];

const JobForm = ({ open, onClose }) => {
  const [customers, setCustomers] = useState([]);
  const [formData, setFormData] = useState({
    customer: "",
    stage: "",
    created_at: "",
    city: "",
    address: "",
  });

  useEffect(() => {
    api
      .get("/api/customer/list/")
      .then((response) => setCustomers(response.data))
      .catch((error) => console.error("Error fetching customers:", error));
  }, []);

  const handleCustomerChange = (event, value) => {
    setFormData({
      ...formData,
      customer: value ? value.id : "",
    });
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = () => {
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
    <Form
      title="Nuova Comessa"
      onSubmit={handleSubmit}
      open={open}
      onClose={onClose}
    >
      <FormControl fullWidth margin="normal">
        <Autocomplete
          options={customers}
          getOptionLabel={(option) => `${option.name} ${option.surname}`}
          onChange={handleCustomerChange}
          renderInput={(params) => <TextField {...params} label="Customer" />}
        />
      </FormControl>
      <FormControl fullWidth margin="normal">
        <InputLabel>Città</InputLabel>
        <Select name="city" value={formData.city} onChange={handleChange}>
          {cities.map((city) => (
            <MenuItem key={city} value={city}>
              {city}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <FormControl fullWidth margin="normal">
        <TextField
          label="Via"
          name="address"
          value={formData.address}
          onChange={handleChange}
        />
      </FormControl>
    </Form>
  );
};

JobForm.propTypes = {
  open: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
};

export default JobForm;
