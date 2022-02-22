import Button from "@material-ui/core/Button";
import Menu from "@material-ui/core/Menu";
import MenuItem from "@material-ui/core/MenuItem";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import React, { useState } from "react";

function NavBarSelect(props) {
  const [menu, setMenu] = useState(null);

  const handleMenuClose = () => {
    setMenu(null);
  };

  const handleMenuButtonClick = (event) => {
    setMenu(event.currentTarget);
  };

  const handleChoiceItemClick = (choice) => {
    props.handleChoiceChange(choice);
    handleMenuClose();
  };

  return (
    <React.Fragment>
      <Button color="inherit" onClick={handleMenuButtonClick}>
        <span>{props.currentChoice}</span>
        <ExpandMoreIcon fontSize="small" />
      </Button>
      <Menu
        id={`${props.name}-menu`}
        key={`${props.name}-menu`}
        anchorEl={menu}
        open={Boolean(menu)}
        onClose={handleMenuClose}
      >
        {props.choices.map((choice) => (
          <MenuItem
            key={choice}
            selected={props.currentChoice === choice}
            onClick={() => {
              handleChoiceItemClick(choice);
            }}
          >
            {choice}
          </MenuItem>
        ))}
      </Menu>
    </React.Fragment>
  );
}

export default NavBarSelect;
