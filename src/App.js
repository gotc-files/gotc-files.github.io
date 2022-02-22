import { createTheme, ThemeProvider } from "@material-ui/core/styles";
import { cyan } from "@material-ui/core/colors";
import Armory from "./pages/Armory";

const theme = createTheme({
  palette: {
    primary: {
      main: "#0d47a1",
    },
    secondary: cyan,
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Armory />
    </ThemeProvider>
  );
}

export default App;
