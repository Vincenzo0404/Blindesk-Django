import * as React from "react";
import { extendTheme, styled } from "@mui/material/styles";
import DashboardIcon from "@mui/icons-material/Dashboard";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import BarChartIcon from "@mui/icons-material/BarChart";
import DescriptionIcon from "@mui/icons-material/Description";
import PeopleIcon from "@mui/icons-material/People";
import LayersIcon from "@mui/icons-material/Layers";
import SettingsIcon from "@mui/icons-material/Settings";
import { AppProvider } from "@toolpad/core";
import { DashboardLayout } from "@toolpad/core";
import { PageContainer } from "@toolpad/core";
import Grid from "@mui/material/Grid";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";
import { Outlet } from "react-router-dom";
import logo from "../assets/logo-trasparente.png";

const NAVIGATION = [
  {
    kind: "header",
    title: "Menu",
  },
  {
    segment: "customers",
    title: "customers",
    icon: <DashboardIcon />,
  },
  // {
  //   segment: "orders",
  //   title: "Orders",
  //   icon: <ShoppingCartIcon />,
  // },
  // {
  //   kind: "divider",
  // },
  // {
  //   kind: "header",
  //   title: "Analytics",
  // },
  // {
  //   segment: "reports",
  //   title: "Reports",
  //   icon: <BarChartIcon />,
  //   children: [
  //     {
  //       segment: "sales",
  //       title: "Sales",
  //       icon: <DescriptionIcon />,
  //     },
  //     {
  //       segment: "traffic",
  //       title: "Traffic",
  //       icon: <DescriptionIcon />,
  //     },
  //   ],
  // },
];

const demoTheme = extendTheme({
  colorSchemes: { light: true, dark: true },
  colorSchemeSelector: "class",
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 600,
      lg: 1200,
      xl: 1536,
    },
  },
});

const height = 8;
const Skeleton = styled("div")(({ theme, height }) => ({
  backgroundColor: theme.palette.action.hover,
  borderRadius: theme.shape.borderRadius,
  height,
  content: '" "',
}));

export default function ToolPad(props) {
  const { window } = props;

  return (
    <AppProvider
      navigation={NAVIGATION}
      theme={demoTheme}
      branding={{
        logo: <img src={logo} alt="Blindesk logo" />,
        title: "... è troppo ponfia!",
        homeUrl: "/customers",
      }}
    >
      <DashboardLayout>
        <PageContainer>
          <Grid container spacing={1}>
            <Outlet />
          </Grid>
        </PageContainer>
      </DashboardLayout>
    </AppProvider>
  );
}
