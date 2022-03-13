import {
  createTheme,
  ThemeProvider,
  StyledEngineProvider,
} from "@mui/material/styles";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Armory from "./pages/Armory";
import Home from "./pages/Home";

const theme = createTheme();

function App() {
  return (
    <BrowserRouter>
      <StyledEngineProvider injectFirst>
        <ThemeProvider theme={theme}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/armory" element={<Armory />} />
            <Route path="/armory/:armoryId" element={<Armory />} />
          </Routes>
        </ThemeProvider>
      </StyledEngineProvider>
    </BrowserRouter>
  );
}

export default App;
