import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
} from "@mui/material";
import PropTypes from "prop-types";

const Form = ({ title, children, onSubmit, open, onClose }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit();
    onClose();
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>{title}</DialogTitle>
      <DialogContent>
        <form onSubmit={handleSubmit}>{children}</form>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} variant="outlined" color="secondary">
          Cancel
        </Button>
        <Button
          onClick={handleSubmit}
          type="submit"
          variant="contained"
          color="primary"
        >
          Submit
        </Button>
      </DialogActions>
    </Dialog>
  );
};

Form.propTypes = {
  title: PropTypes.string.isRequired,
  children: PropTypes.node.isRequired,
  onSubmit: PropTypes.func.isRequired,
  open: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
};

export default Form;
