import {
  DataGrid,
  GridToolbarContainer,
  GridActionsCellItem,
} from "@mui/x-data-grid";
import { CircularProgress } from "@mui/material";
import Button from "@mui/material/Button";
import AddIcon from "@mui/icons-material/Add";
import DeleteIcon from "@mui/icons-material/DeleteOutlined";
import { useState, useEffect } from "react";
import api from "../api";

export default function DataTable({ rows: initialRows, modelName }) {
  const [rows, setRows] = useState(initialRows);
  const [loading, setLoading] = useState(true);
  const [rowModesModel, setRowModesModel] = useState({});
  // Table initialization
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
  columns.push({
    field: "actions",
    type: "actions",
    headerName: "Actions",
    width: 100,
    cellClassName: "actions",
    getActions: ({ id }) => {
      return [
        <GridActionsCellItem
          icon={<DeleteIcon />}
          label="Delete"
          onClick={handleDeleteClick(id)}
          color="inherit"
        />,
      ];
    },
  });

  // Handling requests
  function EditToolbar(props) {
    const { setRows, setRowModesModel } = props;

    const handleAddClick = async () => {
      const newModel = {};

      try {
        const response = await api.post(`/api/${modelName}/create/`, newModel);
        const createdModel = response.data;

        setRows((oldRows) => [...oldRows, createdModel]);
        setRowModesModel((oldModel) => ({
          ...oldModel,
        }));
      } catch (error) {
        console.error(`error during ${modelName} creation:`, error);
      }
    };

    return (
      <GridToolbarContainer>
        <Button
          color="primary"
          startIcon={<AddIcon />}
          onClick={handleAddClick}
        >
          Add record
        </Button>
      </GridToolbarContainer>
    );
  }
  const handleDeleteClick = (id) => async () => {
    try {
      await api.delete(`/api/${modelName}/delete/${id}/`);
      const updatedRows = rows.filter((row) => row.id !== id);
      setRows(updatedRows);
    } catch (error) {
      console.error(`Error during ${modelName} delete:`, error);
    }
  };

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
          slots={{ toolbar: EditToolbar }}
          slotProps={{
            toolbar: { setRows, setRowModesModel },
          }}
          initialState={{
            sorting: {
              sortModel: [{ field: "id", sort: "desc" }],
            },
          }}
        />
      )}
    </div>
  );
}
