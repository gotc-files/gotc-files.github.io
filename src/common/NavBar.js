import MenuIcon from "@mui/icons-material/Menu";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import {
  Box,
  Divider,
  Drawer,
  List,
  ListItemButton,
  ListItemText,
} from "@mui/material";
import AppBar from "@mui/material/AppBar";
import IconButton from "@mui/material/IconButton";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import NavBarSelect from "./NavBarSelect";

const drawerWidth = 240;

function NavBar(props) {
  const [mobileOpen, setMobileOpen] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };
  const topLevelPath = location.pathname.split("/")[1];

  const drawer = (
    <div>
      <Toolbar sx={{ height: props.height }}>
        <Typography variant="h6" sx={{ ml: 1, mr: 5, my: 1, color: "inherit" }}>
          GoTC Files
        </Typography>
      </Toolbar>
      <Divider />
      <List sx={{ py: 0 }}>
        {[
          ["armory", "Armory"],
          ["trinket-armory", "Trinket Armory"],
          ["hero", "Hero"],
          ["hero-collection-action", "Hero Collection Action"],
          ["summon", "Summon"],
          ["daily-delivery", "Daily Delivery"],
          ["building", "Building"],
          ["enhancement", "Enhancement"],
          ["research", "Research"],
        ].map(([url, text]) => (
          <ListItemButton
            key={url}
            component={Link}
            to={`/${url}`}
            selected={topLevelPath === url}
          >
            <ListItemText primary={text} />
          </ListItemButton>
        ))}
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
        <Toolbar sx={{ height: props.height }}>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: "none" } }}
          >
            <MenuIcon />
          </IconButton>
          {props.backLink && (
            <IconButton
              size="large"
              color="inherit"
              onClick={() => {
                navigate(props.backLink);
              }}
            >
              <ArrowBackIcon />
            </IconButton>
          )}
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
            height: props.height,
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
            height: props.height,
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
