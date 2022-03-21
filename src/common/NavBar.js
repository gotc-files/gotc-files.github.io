import MenuIcon from "@mui/icons-material/Menu";
import {
  Box,
  Divider,
  Drawer,
  List,
  ListItem,
  ListItemText,
} from "@mui/material";
import AppBar from "@mui/material/AppBar";
import IconButton from "@mui/material/IconButton";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import React, { useState } from "react";
import { Link } from "react-router-dom";
import NavBarSelect from "./NavBarSelect";

const drawerWidth = 240;

function NavBar(props) {
  const [mobileOpen, setMobileOpen] = useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const drawer = (
    <div>
      <Toolbar>
        <Typography variant="h6" sx={{ ml: 1, mr: 5, my: 1, color: "inherit" }}>
          GoTC Files
        </Typography>
      </Toolbar>
      <Divider />
      <List>
        <ListItem button key="armory" component={Link} to="/armory">
          <ListItemText primary="Armory" />
        </ListItem>
        <ListItem
          button
          key="trinket-armory"
          component={Link}
          to="/trinket-armory"
        >
          <ListItemText primary="Trinket Armory" />
        </ListItem>
      </List>
    </div>
  );

  return (
    <React.Fragment>
      <AppBar
        position="fixed"
        sx={{
          width: { sm: `calc(100% - ${drawerWidth}px)` },
          ml: { sm: `${drawerWidth}px` },
        }}
      >
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: "none" } }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" sx={{ ml: 1, mr: 5, my: 1, color: "white" }}>
            {props.title}
          </Typography>
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
      <Box
        component="nav"
        sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
      >
        <Drawer
          variant="temporary"
          open={mobileOpen}
          onClose={handleDrawerToggle}
          ModalProps={{
            keepMounted: true,
          }}
          sx={{
            display: { xs: "block", sm: "none" },
            "& .MuiDrawer-paper": {
              boxSizing: "border-box",
              width: drawerWidth,
            },
          }}
        >
          {drawer}
        </Drawer>
        <Drawer
          variant="permanent"
          sx={{
            display: { xs: "none", sm: "block" },
            "& .MuiDrawer-paper": {
              boxSizing: "border-box",
              width: drawerWidth,
            },
          }}
          open
        >
          {drawer}
        </Drawer>
      </Box>
    </React.Fragment>
  );
}

export default NavBar;
