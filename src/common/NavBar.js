import { Link as RouterLink } from "react-router-dom";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import NavBarSelect from "./NavBarSelect";
import { Link } from "@mui/material";

function NavBar(props) {
  return (
    <AppBar position="static">
      <Toolbar color="secondary.main">
        <Link to="/" component={RouterLink}>
          <Typography variant="h6" sx={{ ml: 1, mr: 5, my: 1, color: "white" }}>
            {props.title}
          </Typography>
        </Link>
        {(props.selectArgsList || []).map((selectArgs) => (
          <NavBarSelect
            key={selectArgs.name}
            name={selectArgs.name}
            choices={selectArgs.choices}
            currentChoiceId={selectArgs.currentChoiceId}
          />
        ))}
      </Toolbar>
    </AppBar>
  );
}

export default NavBar;
