Name:           intel-vision
Summary:        Metadata package for Intel vision drivers
Version:        2025112.WW46.3_25_ptl_pv
Release:        1%{?dist}
License:        Proprietary
URL:            https://github.com/intel/vision-drivers

BuildRequires:  systemd-rpm-macros
Provides:       intel-vision-kmod-common = %{version}
Requires:       kernel(x86-64) > 6.16.12-200
Requires:       intel-vision-kmod

BuildArch:      noarch

%description
This is the metadata package for IPU7 camera support.

%files

%changelog
* Mon Nov 03 2025 Kate Hsuan <hpa@redhat.com> - 2025112.WW46.3_25_ptl_pv-1
- Meta package for the Intel vision drivers

