import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import Link from "@mui/material/Link";
import Slider from "@mui/material/Slider";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableRow from "@mui/material/TableRow";
import Tooltip from "@mui/material/Tooltip";
import { Box } from "@mui/system";
import React from "react";
import { Link as RouterLink } from "react-router-dom";
import SingleChoiceSelect from "./SingleChoiceSelect";
import { formatData } from "./util";

function getNameTableCell(row) {
  if (row.tooltip) {
    return (
      <Tooltip title={row.tooltip}>{getTableCellMaybeWithLink(row)}</Tooltip>
    );
  } else {
    return getTableCellMaybeWithLink(row);
  }
}

function getTableCellMaybeWithLink(row) {
  if (row.link) {
    return (
      <TableCell size="small">
        <Link component={RouterLink} to={row.link}>
          {row.name}
        </Link>
      </TableCell>
    );
  } else {
    return <TableCell size="small">{row.name}</TableCell>;
  }
}

function getValueTableCell(row) {
  if (row.valueType) {
    return (
      <Tooltip title={row.value.toLocaleString()}>
        <TableCell size="small" align="right">
          {formatData(row.value, row.valueType)}
        </TableCell>
      </Tooltip>
    );
  }
  return (
    <TableCell size="small" align="right">
      {formatData(row.value)}
    </TableCell>
  );
}

function DataCard(props) {
  return (
    <Card>
      <CardHeader
        sx={{ color: "white", backgroundColor: props.color, width: "100%" }}
        title={props.title}
        titleTypographyProps={{ variant: "h6", noWrap: true, width: "100%" }}
        subheader={props.subtitle}
        subheaderTypographyProps={{ color: "inherit", noWrap: true }}
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
        {props.slider && (
          <Box sx={{ px: 3, py: 0.5 }}>
            <Slider
              defaultValue={props.slider.max}
              valueLabelDisplay="auto"
              step={1}
              min={props.slider.min}
              max={props.slider.max}
              value={props.slider.value}
              sx={{ color: props.color }}
              onChange={(e, newValue) => {
                props.slider.setValue(newValue);
              }}
            />
          </Box>
        )}
        {props.select && (
          <Box sx={{ px: 1, py: 0.5 }}>
            <SingleChoiceSelect
              name={props.select.name}
              choices={props.select.choices}
              currentChoice={props.select.currentChoice}
              handleChoiceChange={props.select.handleChoiceChange}
            />
          </Box>
        )}

        <Table>
          <TableBody>
            {props.data.map((row, index) => (
              <TableRow
                key={index}
                sx={{
                  "&:last-child th, &:last-child td": {
                    borderBottom: 0,
                  },
                }}
              >
                {getNameTableCell(row)}
                {getValueTableCell(row)}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  );
}

export default DataCard;
