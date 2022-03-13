import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import NavBarSelect from "./NavBarSelect";

function NavBar(props) {
  return (
    <AppBar position="static">
      <Toolbar color="secondary.main">
        <Typography variant="h6" sx={{ ml: 1, mr: 5, my: 1 }}>
          {props.title}
        </Typography>
        {props.selectArgsList.map((selectArgs) => (
          <NavBarSelect
            key={selectArgs.name}
            name={selectArgs.name}
            choices={selectArgs.choices}
            currentChoice={selectArgs.currentChoice}
            handleChoiceChange={selectArgs.handleChoiceChange}
          />
        ))}
      </Toolbar>
    </AppBar>
  );
}

export default NavBar;
