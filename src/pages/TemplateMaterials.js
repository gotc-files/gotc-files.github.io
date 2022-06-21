import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import TextField from "@mui/material/TextField";

function TemplateMaterials(props) {
  return (
    <Card>
      <CardHeader
        title="Materials"
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
              <TableCell>Name</TableCell>
              {props.qualities.map((quality) => (
                <TableCell size="small">{quality}</TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {props.materials.map((material) => (
              <TableRow
                key={material.id}
                sx={{
                  "&:last-child td, &:last-child th": { border: 0 },
                }}
              >
                <TableCell>{material.name}</TableCell>
                {props.qualities.map((_, qualityIndex) => (
                  <TableCell size="small" sx={{ minWidth: 70 }}>
                    <TextField
                      size="small"
                      margin="dense"
                      variant="standard"
                      value={props.existingMaterials[material.id][qualityIndex]}
                      onChange={(e) =>
                        props.setExistingMaterials({
                          ...props.existingMaterials,
                          [material.id]: props.existingMaterials[
                            material.id
                          ].map((currentValue, currentIndex) =>
                            currentIndex === qualityIndex
                              ? e.target.value
                              : currentValue
                          ),
                        })
                      }
                    />
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  );
}

export default TemplateMaterials;
