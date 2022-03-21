import { Box, Container } from "@mui/material";
import NavBar from "./NavBar";

function Page(props) {
  return (
    <Box sx={{ display: "flex" }}>
      <NavBar
        height={56}
        title={props.title}
        selectArgsList={props.selectArgsList}
      />
      <Container maxWidth="lg" sx={{ mt: "64px" }}>
        {props.children}
      </Container>
    </Box>
  );
}

export default Page;
