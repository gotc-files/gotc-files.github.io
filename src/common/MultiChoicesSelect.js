import {
  Checkbox,
  FormControl,
  InputLabel,
  ListItemText,
  MenuItem,
  OutlinedInput,
  Select,
} from "@mui/material";

function formatLabel(name) {
  return name
    .split("-")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

function MultiChoicesSelect(props) {
  const handleChange = (event) => {
    const {
      target: { value: selectedChoices },
    } = event;
    props.handleChoicesChange(
      typeof selectedChoices === "string"
        ? selectedChoices.split(",")
        : selectedChoices
    );
  };

  return (
    <FormControl sx={{ m: 1, width: 300 }}>
      <InputLabel id={props.name + "-label"}>
        {formatLabel(props.name)}
      </InputLabel>
      <Select
        labelId={props.name + "-label"}
        id={props.name}
        multiple
        value={props.selectedChoices}
        onChange={handleChange}
        input={<OutlinedInput label={formatLabel(props.name)} />}
        renderValue={(selected) => selected.join(", ")}
      >
        {props.choices.map((choice, index) => (
          <MenuItem key={index} value={choice}>
            <Checkbox checked={props.selectedChoices.includes(choice)} />
            <ListItemText primary={choice} />
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}

export default MultiChoicesSelect;
