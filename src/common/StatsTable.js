import { CardContent, Tooltip } from "@mui/material";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableRow from "@mui/material/TableRow";
import React from "react";

function formatNumber(num) {
  if (num === Math.floor(num) && num > 10) {
    return num;
  }
  return `${Math.floor(num * 10000) / 100}%`;
}

function StatsTable(props) {
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
        <Table>
          <TableBody>
            {props.stats.map((stats, index) => (
              <TableRow
                key={index}
                sx={{
                  "&:last-child th, &:last-child td": {
                    borderBottom: 0,
                  },
                }}
              >
                <Tooltip title={stats.description}>
                  <TableCell size="small">{stats.name}</TableCell>
                </Tooltip>
                <TableCell size="small" align="right">
                  {formatNumber(stats.value)}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  );
}

export default StatsTable;
