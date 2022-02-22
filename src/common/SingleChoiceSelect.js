import {
  FormControl,
  InputLabel,
  makeStyles,
  MenuItem,
  Select,
} from "@material-ui/core";

function formatLabel(name) {
  return name
    .split("-")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

const useStyles = makeStyles((theme) => ({
  select: {
    margin: theme.spacing(1),
    minWidth: 100,
  },
}));

function SingleChoiceSelect(props) {
  const classes = useStyles();
  const handleChange = (event) => {
    props.handleChoiceChange(event.target.value);
  };

  return (
    <FormControl className={classes.select}>
      <InputLabel id={props.name} color="primary">
        {formatLabel(props.name)}
      </InputLabel>
      <Select
        labelId={`${props.name}-label`}
        id={props.name}
        value={props.currentChoice}
        label={props.name}
        onChange={handleChange}
      >
        {props.choices.map((choice) => (
          <MenuItem value={choice} key={choice}>
            {choice}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}

export default SingleChoiceSelect;
