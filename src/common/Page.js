import { Box, Container } from "@mui/material";
import NavBar from "./NavBar";

function Page(props) {
  return (
    <Box sx={{ display: "flex" }}>
      <NavBar
        drawerWidth={240}
        height={80}
        title={props.title}
        backLink={props.backLink}
        selectArgsList={props.selectArgsList}
      />
      <Box
        sx={{
          mt: "80px",
          position: "absolute",
          left: { sm: "240px", xs: 0 },
          right: 0,
        }}
      >
        <Container>{props.children}</Container>
      </Box>
    </Box>
  );
}

export default Page;
