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
  title: PropTypes.string,
  children: PropTypes.node,
  onSubmit: PropTypes.func,
  open: PropTypes.bool,
  onClose: PropTypes.func,
};

export default Form;
