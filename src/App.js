import { blue, cyan } from "@mui/material/colors";
import {
  createTheme,
  StyledEngineProvider,
  ThemeProvider,
} from "@mui/material/styles";
import { HashRouter, Route, Routes } from "react-router-dom";
import Armory from "./pages/Armory";
import Building from "./pages/Building";
import DailyDeliveryDetails from "./pages/DailyDeliveryDetails";
import DailyDeliveryTable from "./pages/DailyDeliveryTable";
import Enhancement from "./pages/Enhancement";
import Hero from "./pages/Hero";
import HeroCollectionAction from "./pages/HeroCollectionAction";
import Home from "./pages/Home";
import ResearchDetails from "./pages/ResearchDetails";
import ResearchTable from "./pages/ResearchTable";
import Summon from "./pages/Summon";
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
            <Route
              path="/hero-collection-action"
              element={<HeroCollectionAction />}
            />
            <Route path="/summon" element={<Summon />} />
            <Route path="/summon/:timeStrName" element={<Summon />} />
            <Route path="/daily-delivery" element={<DailyDeliveryTable />} />
            <Route
              path="/daily-delivery/:packId"
              element={<DailyDeliveryDetails />}
            />
            <Route path="/building" element={<Building />} />
            <Route path="/enhancement" element={<Enhancement />} />
            <Route path="/research" element={<ResearchTable />} />
            <Route path="/research/:researchId" element={<ResearchDetails />} />
          </Routes>
        </ThemeProvider>
      </StyledEngineProvider>
    </HashRouter>
  );
}

export default App;
