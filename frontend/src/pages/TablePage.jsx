/* eslint-disable react/prop-types */
import { useState, useEffect } from "react";
import api from "../api";
import { CircularProgress, Alert } from "@mui/material";
import DataTable from "../components/DataTable";

function TablePage({ modelName }) {
  const [dataSet, setDataSet] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    api
      .get(`/api/${modelName}/list/`)
      .then((response) => response.data)
      .then((data) => {
        setDataSet(data);
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

  return <DataTable rows={dataSet} modelName={modelName} />;
}

export default TablePage;
