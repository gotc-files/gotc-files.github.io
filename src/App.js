import { blue, cyan } from "@mui/material/colors";
import {
  createTheme,
  StyledEngineProvider,
  ThemeProvider,
} from "@mui/material/styles";
import { HashRouter, Route, Routes } from "react-router-dom";
import Armory from "./pages/Armory";
import Hero from "./pages/Hero";
import Home from "./pages/Home";
import TrinketArmory from "./pages/TrinketArmory";

const theme = createTheme({
  palette: {
    primary: blue,
    secondary: cyan,
    poor: {
      main: "#fefefe",
    },
    common: {
      main: "#6ad812",
    },
    fine: {
      main: "#2892dc",
    },
    exquisite: {
      main: "#d536db",
    },
    epic: {
      main: "#fe7d0e",
    },
    legendary: {
      main: "#ffff0d",
    },
  },
});

function App() {
  return (
    <HashRouter>
      <StyledEngineProvider injectFirst>
        <ThemeProvider theme={theme}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/armory" element={<Armory />} />
            <Route path="/armory/:armoryId" element={<Armory />} />
            <Route path="/trinket-armory" element={<TrinketArmory />} />
            <Route
              path="/trinket-armory/:trinketArmoryId"
              element={<TrinketArmory />}
            />
            <Route path="/hero" element={<Hero />} />
          </Routes>
        </ThemeProvider>
      </StyledEngineProvider>
    </HashRouter>
  );
}

export default App;
