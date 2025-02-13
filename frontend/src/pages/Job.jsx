import { useState, useEffect } from "react";
import api from "../api";
import {
  Grid,
  Card,
  CardContent,
  Typography,
  MenuItem,
  Select,
  FormControl,
  InputLabel,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
} from "@mui/material";
import JobForm from "../components/JobForm";

export default function OrderGrid() {
  const [jobs, setJobs] = useState([]);
  const [sortType, setSortType] = useState("date"); // Ordinamento predefinito
  const [open, setOpen] = useState(false);

  useEffect(() => {
    api
      .get(`/api/job/list/`)
      .then((response) => response.data)
      .then((data) => {
        setJobs(data);
      });
  }, []);

  const handleSortChange = (event) => {
    const sortBy = event.target.value;
    setSortType(sortBy);

    const sortedjobs = [...jobs].sort((a, b) => {
      if (sortBy === "created_at")
        return new Date(b.created_at) - new Date(a.created_at);
      if (sortBy === "stage") return a.stage.localeCompare(b.stage);
      return 0;
    });

    setJobs(sortedjobs);
  };

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
    api
      .get(`/api/job/list/`)
      .then((response) => response.data)
      .then((data) => {
        setJobs(data);
      });
  };

  return (
    <div style={{ padding: "20px" }}>
      {/* Select per ordinamento */}
      <FormControl sx={{ minWidth: 200, marginBottom: 2 }}>
        <InputLabel>Ordina per</InputLabel>
        <Select value={sortType} onChange={handleSortChange}>
          <MenuItem value="created_at">Data di creazione</MenuItem>
          <MenuItem value="stage">Stato</MenuItem>
        </Select>
      </FormControl>
      <Button variant="outlined" onClick={handleOpen}>
        + Nuova
      </Button>

      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Nuova Comessa</DialogTitle>
        <DialogContent>
          <JobForm onClose={handleClose} />
        </DialogContent>
      </Dialog>

      {/* Griglia di commesse */}
      <Grid container spacing={2}>
        {jobs.map((job) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={job.id}>
            <Card
              sx={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                minHeight: 120,
              }}
            >
              <CardContent>
                <Typography variant="h6">{`${job.customer_name} ${job.customer_surname}`}</Typography>
                <Typography variant="body2">Stato: {job.stage}</Typography>
                <Typography variant="body2">Data: {job.created_at}</Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );
}
