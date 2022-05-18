import Link from "@mui/material/Link";
import Tooltip from "@mui/material/Tooltip";
import MUIDataTable from "mui-datatables";
import { Link as RouterLink } from "react-router-dom";
import { formatData } from "./util";

function getDataMaybeWithLink(dataEntry, config) {
  if (config.linkAccessor) {
    return (
      <Link component={RouterLink} to={config.linkAccessor(dataEntry)}>
        {config.valueAccessor(dataEntry)}
      </Link>
    );
  }
  return <span>{config.valueAccessor(dataEntry)}</span>;
}

function getDataDisplay(dataEntry, config) {
  if (config.valueType === "text") {
    if (config.tooltipAccessor) {
      return (
        <Tooltip title={config.tooltipAccessor(dataEntry)}>
          {getDataMaybeWithLink(dataEntry, config)}
        </Tooltip>
      );
    } else {
      return getDataMaybeWithLink(dataEntry, config);
    }
  }
  if (config.valueType === "stats") {
    return formatData(config.valueAccessor(dataEntry));
  }
  return (
    <Tooltip title={config.valueAccessor(dataEntry).toLocaleString()}>
      <span>
        {formatData(config.valueAccessor(dataEntry), config.valueType)}
      </span>
    </Tooltip>
  );
}

function DataTable(props) {
  const columns = props.columnConfigs.map((columnConfig) => ({
    name: columnConfig.name,
    options: {
      customBodyRenderLite: (dataIndex) =>
        getDataDisplay(props.data[dataIndex], columnConfig),
      ...columnConfig.options,
    },
  }));
  const data = props.data.map((entry) =>
    props.columnConfigs.map((columnConfig) =>
      columnConfig.valueType === "text" ? columnConfig.valueAccessor(entry) : ""
    )
  );
  return (
    <MUIDataTable
      title={props.title}
      data={data}
      columns={columns}
      options={{
        download: false,
        filter: false,
        print: false,
        jumpToPage: true,
        sort: false,
        selectableRows: "none",
        storageKey: props.storageKey,
        ...props.options,
      }}
    ></MUIDataTable>
  );
}

export default DataTable;
