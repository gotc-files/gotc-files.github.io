import { CardContent } from "@mui/material";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import React from "react";
import StatsTable from "./StatsTable";

function StatsCard(props) {
  return (
    <Card>
      <CardHeader
        style={{ backgroundColor: props.color }}
        sx={{ color: "white" }}
        title={props.title}
        titleTypographyProps={{ variant: "h6" }}
      />
      <CardContent
        sx={{
          pt: 0.5,
          px: 0,
          pb: 0,
          "&:last-child": {
            pb: 0.5,
          },
        }}
      >
        <StatsTable stats={props.stats} />
      </CardContent>
    </Card>
  );
}

export default StatsCard;
