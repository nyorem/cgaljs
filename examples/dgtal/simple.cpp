#include <iostream>
#include <DGtal/helpers/Shortcuts.h>
#include <DGtal/helpers/ShortcutsGeometry.h>

using namespace DGtal;

using SH3 = Shortcuts<Z3i::KSpace>;
using SHG3 = ShortcutsGeometry<Z3i::KSpace>;

int main() {
    auto params = SH3::defaultParameters();
    params("polynomial", "goursat" )( "gridstep", 0.5 )( "colormap", "Tics" );
    auto implicit_shape  = SH3::makeImplicitShape3D  ( params );
    auto digitized_shape = SH3::makeDigitizedImplicitShape3D( implicit_shape, params );
    auto binary_image    = SH3::makeBinaryImage      ( digitized_shape, params );
    auto K               = SH3::getKSpace( params );
    auto surface         = SH3::makeLightDigitalSurface( binary_image, K, params );
    auto surfels         = SH3::getSurfelRange( surface, params );
    auto mean_curv       = SHG3::getMeanCurvatures( implicit_shape, K, surfels, params );
    auto cmap            = SH3::getColorMap( -0.3, 0.3, params );
    auto colors          = SH3::Colors( surfels.size() );
    std::transform( mean_curv.cbegin(), mean_curv.cend(), colors.begin(), cmap );

    std::cout << "OK" << std::endl;

    return 0;
}

