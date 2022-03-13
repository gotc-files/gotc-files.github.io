import {
  createTheme,
  ThemeProvider,
  StyledEngineProvider,
} from "@mui/material/styles";
import { HashRouter, Route, Routes } from "react-router-dom";
import Armory from "./pages/Armory";
import Home from "./pages/Home";

const theme = createTheme();

function App() {
  return (
    <HashRouter>
      <StyledEngineProvider injectFirst>
        <ThemeProvider theme={theme}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/armory" element={<Armory />} />
            <Route path="/armory/:armoryId" element={<Armory />} />
          </Routes>
        </ThemeProvider>
      </StyledEngineProvider>
    </HashRouter>
  );
}

export default App;
