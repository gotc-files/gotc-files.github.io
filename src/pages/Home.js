import React from "react";
import { Navigate } from "react-router-dom";

function Home() {
  return <Navigate replace to="/armory" />;
}

export default Home;
