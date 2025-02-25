import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import NotFound from "./pages/NotFound";
import Customer from "./pages/Customer";
import Products from "./pages/Products";
import Job from "./pages/Job";
import ProtectedRoutes from "./components/ProtectedRoutes";

function Logout() {
  localStorage.clear();
  return <Navigate to="/" />;
}
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route element={<ProtectedRoutes />}>
          <Route path="/" element={<Customer />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/customer" element={<Customer />} />
          <Route path="/job" element={<Job />} />
          <Route path="/products" element={<Products />} />
        </Route>
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
