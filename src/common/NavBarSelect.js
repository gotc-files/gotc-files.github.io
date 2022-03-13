import Button from "@mui/material/Button";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import { ExpandMore } from "@mui/icons-material";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function NavBarSelect(props) {
  const [menu, setMenu] = useState(null);
  let navigate = useNavigate();

  const handleMenuClose = () => {
    setMenu(null);
  };

  const handleMenuButtonClick = (event) => {
    setMenu(event.currentTarget);
  };

  const handleChoiceItemClick = (choice) => {
    handleMenuClose();
    navigate(choice.link);
  };

  return (
    <React.Fragment>
      <Button color="inherit" onClick={handleMenuButtonClick}>
        <span>
          {
            props.choices.find((choice) => choice.id === props.currentChoiceId)
              .name
          }
        </span>
        <ExpandMore fontSize="small" />
      </Button>
      <Menu
        id={`${props.id}-menu`}
        key={`${props.id}-menu`}
        anchorEl={menu}
        open={Boolean(menu)}
        onClose={handleMenuClose}
      >
        {props.choices.map((choice) => (
          <MenuItem
            key={choice.id}
            selected={props.currentChoiceId === choice.id}
            onClick={() => {
              handleChoiceItemClick(choice);
            }}
          >
            {choice.name}
          </MenuItem>
        ))}
      </Menu>
    </React.Fragment>
  );
}

export default NavBarSelect;
