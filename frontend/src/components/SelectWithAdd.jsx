import { useState } from "react";
import {
  Autocomplete,
  TextField,
  IconButton,
  Box,
  ListItem,
  ListItemText,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import PropTypes from "prop-types";

const SelectWithAdd = ({ options, onAdd, onSelect }) => {
  const [value, setValue] = useState(null);

  return (
    <Box display="flex" alignItems="center" width="100%">
      <Autocomplete
        options={options}
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
          onSelect(newValue);
        }}
        getOptionLabel={(option) => option.name} // Mostra il nome dell'opzione
        isOptionEqualToValue={(option, value) => option.id === value.id} // Confronta le opzioni per ID
        renderOption={(props, option) => (
          <ListItem {...props} key={option.id}>
            <ListItemText primary={option.name} />
          </ListItem>
        )}
        renderInput={(params) => (
          <TextField
            {...params}
            label="Select option"
            variant="outlined"
            fullWidth
            InputProps={{
              ...params.InputProps,
              style: { padding: "10px" }, // Aggiungi padding per migliorare la visibilità
            }}
          />
        )}
        style={{ flexGrow: 1, marginRight: 8 }}
      />
      <IconButton onClick={onAdd} color="primary">
        <AddIcon />
      </IconButton>
    </Box>
  );
};

SelectWithAdd.propTypes = {
  options: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
    })
  ).isRequired,
  onAdd: PropTypes.func.isRequired,
  onSelect: PropTypes.func.isRequired,
  onEdit: PropTypes.func.isRequired,
};

export default SelectWithAdd;
