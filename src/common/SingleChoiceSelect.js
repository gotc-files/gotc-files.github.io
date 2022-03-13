import { FormControl, InputLabel, MenuItem, Select } from "@mui/material";

function formatLabel(name) {
  return name
    .split("-")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

function SingleChoiceSelect(props) {
  const handleChange = (event) => {
    props.handleChoiceChange(event.target.value);
  };

  return (
    <FormControl sx={{ margin: 1, minWidth: 100 }}>
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
