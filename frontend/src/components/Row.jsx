import { useState, useEffect } from "react";
import api from "../api";

function Row({ customer }) {
  const [name, setName] = useState(customer.name);
  const [surname, setSurname] = useState(customer.surname);

  return <div></div>;
}
