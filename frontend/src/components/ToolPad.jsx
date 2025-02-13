import * as React from "react";
import { extendTheme, styled } from "@mui/material/styles";
import PersonSharpIcon from "@mui/icons-material/PersonSharp";
import Inventory2Icon from "@mui/icons-material/Inventory2";
import { AppProvider } from "@toolpad/core";
import { DashboardLayout } from "@toolpad/core";
import { PageContainer } from "@toolpad/core";
import Grid from "@mui/material/Grid";
import { Outlet } from "react-router-dom";
import logo from "../assets/logo-trasparente.png";

const NAVIGATION = [
  {
    kind: "header",
    title: "Menu",
  },
  {
    segment: "customer",
    title: "clienti",
    icon: <PersonSharpIcon />,
  },
  {
    segment: "job",
    title: "Commesse",
    icon: <PersonSharpIcon />,
  },
  {
    kind: "divider",
  },
  {
    segment: "category",
    title: "Categorie",
    icon: <Inventory2Icon />,
  },
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
          <Grid container spacing={2}>
            <Outlet />
          </Grid>
        </PageContainer>
      </DashboardLayout>
    </AppProvider>
  );
}
