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
} from "@mui/material";
import JobForm from "../components/JobForm";
import JobDetail from "../components/JobDetail";
import { format } from "date-fns";

export default function OrderGrid() {
  const [jobs, setJobs] = useState([]);
  const [sortType, setSortType] = useState("date"); // Ordinamento predefinito
  const [formOpen, setFormOpen] = useState(false);
  const [detailOpen, setDetailOpen] = useState(false);
  const [selectedJob, setSelectedJob] = useState(null);

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
    setFormOpen(true);
  };

  const handleClose = () => {
    setFormOpen(false);
    api
      .get(`/api/job/list/`)
      .then((response) => response.data)
      .then((data) => {
        setJobs(data);
      });
  };

  const handleJobDetailOpen = (job) => {
    setSelectedJob(job);
    setDetailOpen(true);
  };

  const handleJobDetailClose = () => {
    setDetailOpen(false);
    setSelectedJob(null);
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
      <JobForm open={formOpen} onClose={handleClose} />
      {selectedJob && (
        <JobDetail
          job={selectedJob}
          open={detailOpen}
          onClose={handleJobDetailClose}
        />
      )}

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
              <CardContent onClick={() => handleJobDetailOpen(job)}>
                <Typography variant="h6">{`${job.customer_name} ${job.customer_surname}`}</Typography>
                <Typography variant="body2">Stato: {job.stage}</Typography>
                <Typography variant="body2">
                  Data: {format(new Date(job.created_at), "dd/MM/yyyy")}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );
}
