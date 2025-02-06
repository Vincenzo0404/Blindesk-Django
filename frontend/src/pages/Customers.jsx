import { useState, useEffect } from "react";
import api from "../api";
import { CircularProgress, Alert } from "@mui/material";
import DataTable from "../components/DataTable";

function Customers() {
  const [customers, setCustomers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    api
      .get("/api/customers/")
      .then((response) => response.data)
      .then((data) => {
        setCustomers(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <CircularProgress />;
  }

  if (error) {
    return <Alert severity="error">{error.message}</Alert>;
  }

  return <DataTable rows={customers} />;
}

export default Customers;
