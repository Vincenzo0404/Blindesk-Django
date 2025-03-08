/* eslint-disable react-hooks/exhaustive-deps */
import { useState, useEffect } from "react";
import { DataGrid, GridToolbarContainer } from "@mui/x-data-grid";
import { Alert, Button } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import PropTypes from "prop-types";
import api from "../api";

function EditToolbar({ setRows, modelName, baseModel }) {
  const handleAddClick = async () => {
    try {
      const response = await api.post(`/api/${modelName}/create/`, baseModel);
      const createdModel = response.data;

      setRows((oldRows) => [...oldRows, createdModel]);
    } catch (error) {
      console.error(`Error during ${modelName} creation:`, error);
    }
  };

  return (
    <GridToolbarContainer>
      <Button color="primary" startIcon={<AddIcon />} onClick={handleAddClick}>
        {modelName}
      </Button>
    </GridToolbarContainer>
  );
}

EditToolbar.propTypes = {
  setRows: PropTypes.func.isRequired,
  modelName: PropTypes.string.isRequired,
  baseModel: PropTypes.object.isRequired,
};

export default function DataTable({
  modelName,
  queryParams,
  onRowSelected,
  baseModel = {},
}) {
  const [rows, setRows] = useState([]);
  const [error, setError] = useState(null);
  const [columns, setColumns] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      setError(null);

      const queryString = new URLSearchParams(queryParams).toString();
      const url = `/api/${modelName}/list/${queryString ? `?${queryString}` : ""}`;

      try {
        const response = await api.get(url);
        setRows(response.data);
      } catch (err) {
        setError(err);
      }
    };

    const fetchMetadata = async () => {
      try {
        const response = await api.get(`/api/model-metadata/${modelName}/`);
        const metadata = response.data;

        const columns = metadata.map((field) => ({
          field: field.name,
          headerName: field.name,
          type: field.type === "IntegerField" ? "number" : "string",
          editable: field.name !== "id",
          ...(field.type === "singleSelect" && {
            type: "singleSelect",
            valueOptions: field.choices.map((choice) => ({
              value: choice.id,
              label: choice.display,
            })),
          }),
        }));

        setColumns(columns);
      } catch (err) {
        setError(err);
      }
    };
    fetchMetadata();
    fetchData();
  }, [modelName, queryParams]);

  const handleRowSelection = (selectionModel) => {
    const selectedRow = rows.find((row) => row.id === selectionModel[0]);
    if (selectedRow) {
      onRowSelected(selectedRow);
    }
  };

  // Handling requests
  const saveRowOnServer = async (updatedRow) => {
    try {
      const response = await api.put(
        `/api/${modelName}/update/${updatedRow.id}/`,
        updatedRow
      );

      if (response.status !== 200) {
        throw new Error("Error during row update");
      }

      const updatedRows = rows.map((row) =>
        row.id === updatedRow.id ? updatedRow : row
      );
      setRows(updatedRows);

      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  };

  const handleProcessRowUpdateError = (error) => {
    console.error("Error during row update:", error);
  };

  if (error) {
    return <Alert severity="error">{error.message}</Alert>;
  }

  return (
    <div
      style={{
        height: 500,
        width: "100%",
        display: "flex",
        flexDirection: "column",
      }}
    >
      <DataGrid
        editMode="row"
        rows={rows}
        columns={columns}
        processRowUpdate={(updatedRow) => saveRowOnServer(updatedRow)}
        onProcessRowUpdateError={handleProcessRowUpdateError}
        slots={{ toolbar: EditToolbar }}
        slotProps={{
          toolbar: { setRows, modelName, baseModel },
        }}
        initialState={{
          sorting: {
            sortModel: [{ field: "id", sort: "desc" }],
          },
        }}
        onRowSelectionModelChange={(newSelection) => {
          handleRowSelection(newSelection);
        }}
      />
    </div>
  );
}

DataTable.propTypes = {
  modelName: PropTypes.string.isRequired,
  queryParams: PropTypes.object,
  onRowSelected: PropTypes.func,
  baseModel: PropTypes.object,
};
