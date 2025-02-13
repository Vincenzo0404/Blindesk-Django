import { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css";
import LoadingIndicator from "./LoadingIndicator";

function Form() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from || "/customers"; // Salva la pagina precedente

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setErrorMessage(""); // Reset degli errori

    try {
      const res = await api.post("/api/token/", { username, password });

      // Salvataggio dei token
      localStorage.setItem(ACCESS_TOKEN, res.data.access);
      localStorage.setItem(REFRESH_TOKEN, res.data.refresh);

      navigate(from, { replace: true }); // Redirect alla pagina precedente
    } catch (error) {
      alert(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <h1>Login</h1>
      {errorMessage && <p className="error-message">{errorMessage}</p>}{" "}
      {/* Mostra l'errore */}
      <input
        className="form-input"
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
        disabled={loading} // Disabilitato durante il login
      />
      <input
        className="form-input"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        disabled={loading}
      />
      {loading && <LoadingIndicator />} {/* Indicatore di caricamento */}
      <button className="form-button" type="submit" disabled={loading}>
        {loading ? "Accesso in corso..." : "Login"}
      </button>
    </form>
  );
}

export default Form;
