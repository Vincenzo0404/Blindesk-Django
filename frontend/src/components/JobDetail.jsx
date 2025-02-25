import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import {
  TextField,
  FormControl,
  MenuItem,
  Select,
  InputLabel,
} from "@mui/material";
import api from "../api";
import Form from "./Form";

const JobDetail = ({ job, open, onClose }) => {
  const [status, setStatus] = useState(job.stage);
  const [stageChoices, setStageChoices] = useState([]);

  useEffect(() => {
    api
      .get("/api/job/stage-choices/")
      .then((response) => {
        setStageChoices(response.data);
      })
      .catch((error) => console.error("Error fetching stage choices:", error));
  }, []);

  const handleStatusChange = (event) => {
    setStatus(event.target.value);
  };

  const handleSubmit = () => {
    console.log(job);
    api
      .put(`/api/job/update/${job.id}/`, { stage: status })
      .then((response) => {
        if (response.data.success) {
          onClose();
        } else {
          console.error("Error updating job:", response.data.errors);
        }
      })
      .catch((error) => console.error("Error updating job:", error));
  };

  return (
    <Form
      title="Dettagli Comessa"
      onSubmit={handleSubmit}
      open={open}
      onClose={onClose}
    >
      <FormControl required fullWidth margin="normal">
        <TextField
          label="Cliente"
          value={`${job.customer_name} ${job.customer_surname}`}
          InputProps={{
            readOnly: true,
          }}
        />
      </FormControl>
      <FormControl fullWidth margin="normal">
        <TextField
          label="Data di Creazione"
          value={job.created_at}
          InputProps={{
            readOnly: true,
          }}
        />
      </FormControl>
      <FormControl fullWidth margin="normal">
        <InputLabel>Stato</InputLabel>
        <Select value={status} onChange={handleStatusChange}>
          {stageChoices.map((choice) => (
            <MenuItem key={choice.value} value={choice.value}>
              {choice.label}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Form>
  );
};

JobDetail.propTypes = {
  job: PropTypes.object.isRequired,
  open: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
};

export default JobDetail;
