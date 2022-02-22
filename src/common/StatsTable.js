import { CardContent, makeStyles, Tooltip } from "@material-ui/core";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableRow from "@material-ui/core/TableRow";
import React from "react";

const useStyles = makeStyles((theme) => ({
  header: {
    color: "white",
  },
  content: {
    padding: theme.spacing(0.5, 0, 0, 0),
    "&:last-child": {
      paddingBottom: 0,
    },
  },
  tableRow: {
    "&:last-child th, &:last-child td": {
      borderBottom: 0,
    },
  },
}));

function formatNumber(num) {
  if (num === Math.floor(num) && num > 10) {
    return num;
  }
  return `${Math.floor(num * 10000) / 100}%`;
}

function StatsTable(props) {
  const classes = useStyles();
  return (
    <Card>
      <CardHeader
        className={classes.header}
        style={{ backgroundColor: props.color }}
        title={props.title}
        titleTypographyProps={{ variant: "h6" }}
      />
      <CardContent className={classes.content}>
        <Table>
          <TableBody>
            {props.stats.map((stats, index) => (
              <TableRow key={index} className={classes.tableRow}>
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
