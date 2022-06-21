import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import TextField from "@mui/material/TextField";

function Cell(props) {
  return (
    <TableCell size="small" sx={{ minWidth: 70 }}>
      <TextField
        size="small"
        margin="dense"
        variant="standard"
        value={props.value}
        onChange={props.onChange}
        disabled={props.disabled}
      />
    </TableCell>
  );
}

function TemplateGoals(props) {
  return (
    <Card>
      <CardHeader
        title="Goals"
        sx={{ backgroundColor: "primary.main", color: "white" }}
      ></CardHeader>
      <CardContent
        sx={{
          pt: 0.5,
          px: 0,
          pb: 0,
          "&:last-child": {
            pb: 0.5,
          },
          overflow: "scroll",
        }}
      >
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell>Level</TableCell>
              <TableCell>Goal</TableCell>
              <TableCell>Existing</TableCell>
              <TableCell>To Craft</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {props.existingTemplates.map((numExistingTemplates, index) => (
              <TableRow
                key={index}
                sx={{
                  "&:last-child td, &:last-child th": { border: 0 },
                }}
              >
                <TableCell>{props.levels[index]}</TableCell>
                <Cell value={props.numTemplates} disabled />
                <Cell
                  value={numExistingTemplates}
                  onChange={(e) =>
                    props.setExistingTemplates(
                      props.existingTemplates.map(
                        (currentExistingTemplates, currentIndex) =>
                          currentIndex === index
                            ? e.target.value
                            : currentExistingTemplates
                      )
                    )
                  }
                />
                <Cell
                  value={props.numTemplates - numExistingTemplates}
                  disabled
                />
              </TableRow>
            ))}
            <TableRow
              key={props.existingTemplates.length}
              sx={{ "td, th": { border: 0 } }}
            >
              <TableCell>{props.levels[props.levels.length - 1]}</TableCell>
              <Cell
                value={props.numTemplates}
                onChange={(e) => props.setNumTemplates(e.target.value)}
              />
              <Cell value={0} disabled />
              <Cell value={props.numTemplates} disabled />
            </TableRow>
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  );
}

export default TemplateGoals;
