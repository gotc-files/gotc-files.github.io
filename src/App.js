import {
  createTheme,
  ThemeProvider,
  StyledEngineProvider,
} from "@mui/material/styles";
import Armory from "./pages/Armory";

const theme = createTheme();

function App() {
  return (
    <StyledEngineProvider injectFirst>
      <ThemeProvider theme={theme}>
        <Armory />
      </ThemeProvider>
    </StyledEngineProvider>
  );
}

export default App;
