import { makeStyles } from "@material-ui/core";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import NavBarSelect from "./NavBarSelect";

const useStyles = makeStyles((theme) => ({
  navTitle: {
    margin: theme.spacing(1, 5, 1, 1),
  },
}));

function NavBar(props) {
  const classes = useStyles();
  return (
    <AppBar position="static">
      <Toolbar color="secondary.main">
        <Typography className={classes.navTitle} variant="h6">
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
