import Button from "@mui/material/Button";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import { ExpandMore } from "@mui/icons-material";
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
        <ExpandMore fontSize="small" />
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
