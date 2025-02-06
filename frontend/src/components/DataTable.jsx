import { DataGrid } from "@mui/x-data-grid";
import { CircularProgress } from "@mui/material";
import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import api from "../api";

export default function DataTable({ rows: initialRows }) {
  const [rows, setRows] = useState(initialRows);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (initialRows && initialRows.length > 0) {
      setRows(initialRows);
      setLoading(false);
    }
  }, [initialRows]);

  const columns =
    rows && rows.length > 0
      ? Object.keys(rows[0]).map((key) => {
          return { field: key, editable: key !== "id" };
        })
      : [];

  const saveRowOnServer = async (updatedRow) => {
    try {
      const response = await api.put(
        `/api/customers/${updatedRow.id}/update/`,
        updatedRow
      );

      if (response.status !== 200) {
        throw new Error("Errore durante l'aggiornamento del cliente");
      }

      const updatedRows = rows.map((row) =>
        row.id === updatedRow.id ? updatedRow : row
      );
      setRows(updatedRows);

      return response.data;
    } catch (error) {
      console.error("Errore:", error);
      throw error;
    }
  };

  const handleProcessRowUpdateError = (error) => {
    console.error("Errore durante l'aggiornamento della riga:", error);
  };

  return (
    <div
      style={{
        height: 500,
        width: "100%",
        display: "flex",
        flexDirection: "column",
      }}
    >
      {loading ? (
        <CircularProgress />
      ) : (
        <DataGrid
          editMode="row"
          rows={rows}
          columns={columns}
          processRowUpdate={(updatedRow, originalRow) =>
            saveRowOnServer(updatedRow)
          }
          onProcessRowUpdateError={handleProcessRowUpdateError}
        />
      )}
    </div>
  );
}

DataTable.propTypes = {
  rows: PropTypes.arrayOf(PropTypes.object).isRequired,
};
