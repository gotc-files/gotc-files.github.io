import { Table, TableBody, TableCell, TableRow, Tooltip } from "@mui/material";

function formatNumber(num) {
  if (num === Math.floor(num) && num > 10) {
    return num;
  }
  return `${Math.floor(num * 10000) / 100}%`;
}

function StatsTable(props) {
  return (
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
  );
}

export default StatsTable;
